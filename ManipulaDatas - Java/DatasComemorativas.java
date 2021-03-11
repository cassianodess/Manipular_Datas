import java.util.ArrayList;

public class DatasComemorativas {

    // Atributo
    private ArrayList<DataComemorativa> feriados = new ArrayList<DataComemorativa>();

    // Metodos
    public void adiciona(DataComemorativa feriado) {

        this.feriados.add(feriado);

    }

    public void remove(String nome) {
        for (int i = 0; i < feriados.size(); i++) {
            if (feriados.get(i).getNome().equals(nome.toUpperCase())) {
                feriados.remove(i);
            }
        }
    }

    public int horasNaoTrabalhodas() {
        return this.feriados.size() * 8;

    }
}
