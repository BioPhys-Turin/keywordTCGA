[![DOI](https://zenodo.org/badge/DOI/10.TBA/TBA.svg)](https://doi.org/TBA)


# A Keywords..

Notebooks and libraries for "..."

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

# License
Please see [LICENSE](LICENSE)
