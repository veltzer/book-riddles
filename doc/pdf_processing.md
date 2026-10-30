# Issues having to do with the quality of the pdf produced

- The version coming out of our pdf production pipeline is 1.4.
  (you can use 'pdfinfo(1)' on the output to see this).
- There are also no author markings on the pdf itself.
  (you can use 'pdfinfo(1)' on the output to see this).
- The output is not serialized for the web (optimized).
  (you can use 'pdfinfo(1)' on the output to see this).
- You can use the 'qpdf' tool to fix some of that (optimized for instance
  and set the versino to 1.5).
  use:

    ```bash
    qpdf --linearize --force-version=1.5 [in.pdf] [out.pdf]
    ```
