public class Karyawan {
    private String nama;
    private int umur;
    private String alamat;

    // Constructor tanpa parameter
    public Karyawan() {
    }

    // Constructor dengan parameter nama
    public Karyawan(String nama) {
        this.nama = nama;
    }

    // Constructor dengan parameter nama dan umur
    public Karyawan(String nama, int umur) {
        this.nama = nama;
        this.umur = umur;
    }

    // Constructor dengan parameter nama, umur, dan alamat
    public Karyawan(String nama, int umur, String alamat) {
        this.nama = nama;
        this.umur = umur;
        this.alamat = alamat;
    }

    // Metode getter dan setter untuk variabel instance (nama, umur, alamat) bisa ditambahkan di sini
}