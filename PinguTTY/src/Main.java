import javax.swing.*;
import java.awt.*;
import java.awt.datatransfer.StringSelection;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class Main {
    public static void main(String[] args) {
        // Crear el JFrame principal (La ventana grande)
        JFrame frame = new JFrame("PinguTTY");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 400);
        frame.setLocationRelativeTo(null);  // Aquí hacemos que esté centradito

        // GridBagLayout para organizar los componentes en una cuadrícula de celdas
        JPanel mainPanel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(10, 10, 10, 10);

        // Botón de Instrucciones
        JButton instructionsButton = new JButton("Instrucciones");
        instructionsButton.setFont(new Font("Arial", Font.PLAIN, 14));
        instructionsButton.setBackground(new Color(0x3498db));
        instructionsButton.setForeground(Color.WHITE);
        instructionsButton.setFocusPainted(false);
        instructionsButton.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(Color.DARK_GRAY),
                BorderFactory.createEmptyBorder(5, 10, 5, 10)
        ));
        instructionsButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                mostrarInstrucciones(frame);
            }
        });

        // Añadir el botón de Instrucciones al panel principal
        gbc.gridx = 0;
        gbc.gridy = 0;
        gbc.anchor = GridBagConstraints.WEST;
        mainPanel.add(instructionsButton, gbc);

        JLabel title = new JLabel("PinguTTY");
        title.setFont(new Font("Arial", Font.BOLD, 24));
        title.setForeground(new Color(0x3498db));  // Color azul
        gbc.gridx = 1;
        gbc.gridy = 0;
        gbc.gridwidth = 2;
        gbc.anchor = GridBagConstraints.CENTER;
        mainPanel.add(title, gbc);

        // Crear los botones con sus textos y colores personalizados
        JButton button1 = createCustomButton("Paso 1", new Color(0x2ecc71));
        JButton button3 = createCustomButton("Paso 2", new Color(0xe74c3c));
        JButton button4 = createCustomButton("Paso 3", new Color(0xf1c40f));
        JButton button5 = createCustomButton("Paso 4", new Color(0x9b59b6));

        // Añadir los botones al panel principal
        gbc.gridwidth = 1;
        gbc.anchor = GridBagConstraints.CENTER;
        gbc.gridx = 0;
        gbc.gridy = 1;
        mainPanel.add(button1, gbc);
        gbc.gridx = 1;
        mainPanel.add(button3, gbc);
        gbc.gridx = 0;
        gbc.gridy = 2;
        mainPanel.add(button4, gbc);
        gbc.gridx = 1;
        mainPanel.add(button5, gbc);

        // Añadir el panel principal al frame
        frame.add(mainPanel);

        // Crear ActionListeners para incrustar cada comando al portapapeles
        button1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                copiarTextoYMostrarMensaje("script /dev/null -c bash", frame);
            }
        });

        button3.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                copiarTextoYMostrarMensaje("stty raw -echo; fg", frame);
            }
        });

        button4.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                copiarTextoYMostrarMensaje("reset xterm", frame);
            }
        });

        button5.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                copiarTextoYMostrarMensaje("export SHELL=bash && export TERM=xterm", frame);
            }
        });

        // Hacer visible el frame
        frame.setVisible(true);
    }

    // Método para copiar texto al portapapeles y mostrar un mensaje
    public static void copiarTextoYMostrarMensaje(String mensaje, JFrame frame) {
        // Copiar el mensaje al portapapeles
        StringSelection stringSelection = new StringSelection(mensaje);
        Toolkit.getDefaultToolkit().getSystemClipboard().setContents(stringSelection, null);
        // Mostrar mensaje al usuario
        JOptionPane.showMessageDialog(frame, "Copiado al portapapeles: " + mensaje);
    }

    // Método para crear un botón personalizado
    private static JButton createCustomButton(String text, Color color) {
        JButton button = new JButton(text);
        button.setFont(new Font("Arial", Font.BOLD, 16));
        button.setBackground(color);
        button.setForeground(Color.WHITE);
        button.setFocusPainted(false);
        button.setBorder(BorderFactory.createCompoundBorder(
                BorderFactory.createLineBorder(Color.DARK_GRAY),
                BorderFactory.createEmptyBorder(10, 20, 10, 20)
        ));
        return button;
    }

    // Método para mostrar las instrucciones
    private static void mostrarInstrucciones(JFrame frame) {
        String instrucciones = "Estas son las instrucciones de uso:\n"
                + "Aplicación para vagos, de tal forma que puedan hacer el tratamiento de la TTY copiando y pegando\n"
                + "Cada vez que se haga clic en uno de los pasos, el comando se copiará al portapapeles";
        JOptionPane.showMessageDialog(frame, instrucciones, "Instrucciones", JOptionPane.INFORMATION_MESSAGE);
    }
}
