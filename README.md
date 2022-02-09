[![DOI](https://zenodo.org/badge/DOI/10.1101/2021.12.22.473851.svg)](https://doi.org/10.1101/2021.12.22.473851)

# Multi-omics topic odeling for breast cancer

Notebooks and libraries for "Multi-omics Topic Modeling for Breast Cancer Classification"

# Run
You can simply create a Docker container with all dependencies installed

```bash
docker run -v $PWD:/home/jovyan/work -p 8888:8888 --rm -it --name topic_tcga docker.pkg.github.com/fvalle1/keywordTCGA/image:latest
```

then point your browser to [localhost](http://localhost:8888)

# Data
The data processed in our analysis when not available trough git can be accessed via [DataVersionControl](https://dvc.org)
```bash
dvc pull -r mydrive
```

# Tool
This paper comes with the [nsbm](https://github.com/fvalle1/nsbm/) tool available which enables the possibility of running multi omics topic modeling on many kind of data.

# License
Please see [LICENSE](LICENSE)
