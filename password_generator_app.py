from mylib.password_generator import creating_password
import gradio as gr

with gr.Blocks() as demo:
    gr.Markdown("# Generate Password")
    length = gr.Textbox(label="Length")
    special_character = gr.Textbox(label="Special Character ?")
    output = gr.Textbox(label="Password")
    generate_btn = gr.Button("Generate")
    # pylint: disable=no-member
    generate_btn.click(
        fn=creating_password,
        inputs=[length, special_character],
        outputs=output,
        api_name="Generate Password",
    )

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    demo.launch()
