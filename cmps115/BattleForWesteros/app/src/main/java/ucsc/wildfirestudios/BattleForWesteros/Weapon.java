package ucsc.wildfirestudios.BattleForWesteros;

//-------------------------------------------------------------------------------------
// Weapon.java
// Wildfire Studios
// Created by: Khang Tran
// Modified by: 
// Notes: Class to create weapon objects for the player to equip
//-------------------------------------------------------------------------------------

public class Weapon {
    /* DATA --------------------------------------------------------------------------- */
    public String type, name;
    public int minLvl, dmg, def, dur;


    /* CONSTRUCTOR -------------------------------------------------------------------- */
    public Weapon(String inputType, String inputName, int inputMinLvl, int inputDmg, int inputDef, int inputDur) {

        type = inputType;
        name = inputName;
        minLvl = inputMinLvl;
        dmg = inputDmg;
        def = inputDef;
        dur = inputDur;
    }


    /* ACCESS FUNCTIONS --------------------------------------------------------------- */
    public String getType() { return type; }
    public String getName() { return name; }
    public int getMinLvl() { return minLvl; }
    public int getDmg() { return dmg; }
    public int getDef() { return def; }
    public int getDur() { return dur; }


    /* OTHER -------------------------------------------------------------------------- */
    public void printStats() {

        System.out.println("------------------------------" + "\n");
        System.out.println("Item Type: " + type + "\n");
        System.out.println("Name: " + name + "\n");
        System.out.println("Level Requirement: " + minLvl + "\n");
        System.out.println("Damage: " + dmg + "\n");
        System.out.println("Durability: " + dur + "\n");
        System.out.println("------------------------------");
    }
}