public class DataComemorativa extends MinhaData {
    // Atributos
    private boolean fnormal = true, fmundial = true;

    public DataComemorativa(String data, String nome) {
        super(data, nome);
    }

    // Métodos Especiais
    protected boolean getFNormal() {
        return this.fnormal;
    }

    protected void setFNormal(boolean fnormal) {
        this.fnormal = fnormal;

    }

    protected boolean getFMundial() {
        return this.fmundial;
    }

    protected void setFMundial(boolean fmundial) {
        this.fmundial = fmundial;
    }

}
