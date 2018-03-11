public class Human extends Player {
	
	public Human(int posx, int posy, int index, SurvivalGame game, int weaponOrHeal) {
		super(80, 2, posx, posy, index, game);
		
		this.myString = 'H' + Integer.toString(index);
		if (weaponOrHeal == 1){
			this.equipment = new Rifle(this);
		}
		else {
			this.equipment = new Wand(this);
		}
		
	}

	public void teleport() {
		super.teleport();
		if (this.equipment instanceof Rifle){
			((Rifle)this.equipment).enhance();
		}
		else if(this.equipment instanceof Wand){
			((Wand)this.equipment).enhance();
		}
	}
	
	public void distance(int posx, int posy)
	{
		
	}
	
	@Override
	public void askForMove() {
		// TODO Auto-generated method stub
		if (this.equipment instanceof Rifle){
			System.out.println(String.format("You are a human (H%d) using Rifle. (Range: %d, Ammo #: %d, Damage per shot: %d)", this.index, 
					this.equipment.getRange(),((Rifle)this.equipment).getAmmo(),
					this.equipment.getEffect() ));
		}
		else if (this.equipment instanceof Wand){
			System.out.println(String.format("You are a human (H%d) using Wand. (Range: %d, effect: %d)", this.index, 
					this.equipment.getRange() ,this.equipment.getEffect() ));
		}

		super.askForMove();
		
	}

}
