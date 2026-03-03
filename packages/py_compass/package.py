# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCompass(PythonPackage):
    """In-Silico Modeling of Metabolic Heterogeneity using Single-Cell Transcriptomes."""

    git = "https://github.com/YosefLab/Compass/"

    version("2022-04-02", commit="7664cb08466510889f9aafb3271140918ac2bf7e")

    depends_on("py-numpy@1.12:", type=("build", "run"))
    depends_on("py-pandas@0.20:", type=("build", "run"))
    depends_on("py-tqdm@4.11:", type=("build", "run"))
    depends_on("py-python-libsbml@5.13:", type=("build", "run"))
    depends_on("py-six@1.10:", type=("build", "run"))
    depends_on("py-scikit-learn@0.19:", type=("build", "run"))
    depends_on("py-scipy@1.0:", type=("build", "run"))
    depends_on("py-python-igraph@0.9:", type=("build", "run"))
    depends_on("py-leidenalg@0.8.2:", type=("build", "run"))
    depends_on("py-anndata", type=("build", "run"))
    depends_on("py-cplex@12.7.0.0:", type=("build", "run"))
