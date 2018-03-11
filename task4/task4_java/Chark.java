public class Chark extends Player {

	public Chark(int posx, int posy, int index, SurvivalGame game, int weaponOrHeal) {
		super(100, 4, posx, posy, index, game);

		this.myString = "C" + Integer.toString(index);
		if (weaponOrHeal == 1){
			this.equipment = new Axe(this);
		}
		else {
			this.equipment = new Wand(this);
		}

	}

	public void teleport() {
		super.teleport();
		if (this.equipment instanceof Axe){
			((Axe) this.equipment).enhance();
		}
		else if(this.equipment instanceof Wand){
			((Wand)this.equipment).enhance();
		}
	}

	@Override
	public void askForMove() {
		// TODO Auto-generated method stub
		if (this.equipment instanceof Axe){
			System.out.println(String.format("You are a Chark (C%d) using Axe. (Range: %d, Damage: %d)",this.index,
			this.equipment.getRange(), (this.equipment).getEffect()));
		}
		else if (this.equipment instanceof Wand){
			System.out.println(String.format("You are a Chark(C%d) using Wand. (Range %d, effect: %d)", this.index, 
					this.equipment.getRange() ,this.equipment.getEffect() ));
		}
		super.askForMove();
		
	}
}
