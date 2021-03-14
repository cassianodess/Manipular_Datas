public class DataComemorativa extends MinhaData {
    // Atributos
    private boolean fnormal, fmundial;

    public DataComemorativa(String data, String nome, boolean fnormal, boolean fmundial) {
        super(data, nome);
        this.fnormal = fnormal;
        this.fmundial = fmundial;
    }

    // Métodos Especiais
    protected boolean isFNormal() {
        return this.fnormal;
    }

    protected void setFNormal(boolean fnormal) {
        this.fnormal = fnormal;

    }

    protected boolean isFMundial() {
        return this.fmundial;
    }

    protected void setFMundial(boolean fmundial) {
        this.fmundial = fmundial;
    }

}
