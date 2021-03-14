import java.util.ArrayList;

public class DatasComemorativas {

    // Atributo
    private ArrayList<MinhaData> feriados = new ArrayList<MinhaData>();

    // Metodos
    public void adiciona(MinhaData feriado) {

        this.feriados.add(feriado);

    }

    public void remove(String nome) {
        for (int i = 0; i < feriados.size(); i++) {
            if (feriados.get(i).getNome().toUpperCase().equals(nome.toUpperCase())) {
                feriados.remove(i);

            }
        }
    }

    public int horasNaoTrabalhodas() {
        return this.feriados.size() * 8;

    }
}
