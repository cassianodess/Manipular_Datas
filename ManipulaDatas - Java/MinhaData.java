public class MinhaData {
    private int dia, mes, ano;
    private String nome;

    // Construtor
    public MinhaData(int dia, int mes, int ano, String nome) {
        this.dia = dia;
        this.mes = mes;
        this.ano = ano;
        this.nome = nome;

    }

    // 2º Contrutor
    public MinhaData(String data, String nome) {
        this.dia = Integer.parseInt(data.split("/")[0]);
        this.mes = Integer.parseInt(data.split("/")[1]);
        this.ano = Integer.parseInt(data.split("/")[2]);
        this.nome = nome;

    }

    // Métodos públicos
    public String toString() {
        return String.format("%s: %d/%d/%d", this.getNome(), this.getDia(), this.getMes(), this.getAno());
    }

    public int Compara(MinhaData data) {
        if ((this.getDia() == data.dia) && (this.getMes() == data.mes) && (this.getAno() == data.ano)) {
            return 0;

        } else if ((this.getAno() == data.ano)) {
            if (this.getMes() > data.mes) {
                return 1;

            } else {
                return -1;
            }

        } else if (this.getAno() > data.ano) {
            return 1;

        } else {
            return -1;

        }

    }

    // Métodos Especiais

    protected String getNome() {
        return this.nome;
    }

    protected void setNome(String nome) {
        this.nome = nome.toUpperCase();
    }

    protected int getDia() {
        return this.dia;
    }

    protected void setDia(int dia) {
        this.dia = dia;
    }

    protected int getMes() {
        return this.mes;
    }

    protected void setMes(int mes) {
        this.mes = mes;
    }

    protected int getAno() {
        return this.ano;
    }

    protected void setAno(int ano) {
        this.ano = ano;
    }

}
