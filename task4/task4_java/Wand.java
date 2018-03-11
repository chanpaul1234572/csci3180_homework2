public class Wand extends Weapon {
    private static final int WAND_RANGE = 5;
    private static final int AXE_INIT_DAMAEG = 5;
    public Wand(Player owner){
        super(WAND_RANGE, AXE_INIT_DAMAEG, owner);
    }
    
    public void enhance(){
        this.effect += 5;
    }

    @Override
    public void action(int posx, int posy) {
        System.out.println("You are using Wand healing " + posx + " " + posy + ".");
        if (this.owner.pos.distance(posx, posy) <= this.range) {
            Player player = owner.game.getPlayer(posx, posy);
            if (player != null) {
                if (player instanceof Human && this.owner instanceof Human) {
                    player.increaseHealth(this.getEffect());
                    if (player.health > 80) {
                       player.health = 80; 
                    }
                } 
                else if (player instanceof Chark && this.owner instanceof Chark) {
                    player.increaseHealth(this.getEffect());
                    if (player.health > 100) {
                       player.health = 100; 
                    }
                } 
                else {
                    System.out.println("Can not use to heal the different race");
                }
            }
        }
        else {
            System.out.println("out of range");
        }
    }
}