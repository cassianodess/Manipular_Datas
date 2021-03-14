public class Main {
    public static void main(String[] args) {

        MinhaData atual = new MinhaData("14/03/2021", "Atual");
        MinhaData natal = new MinhaData("25/12/2021", "Natal");

        System.out.println(atual.Compara(natal));

        DatasComemorativas feriados = new DatasComemorativas();
        feriados.adiciona(natal);

        System.out.println(feriados.horasNaoTrabalhodas());

        /**
         * Saída1: -1
         * Saída2: 8
         */

    }
}