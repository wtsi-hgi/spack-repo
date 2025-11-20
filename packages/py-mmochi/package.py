# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyMmochi(PythonPackage):
    """MMoCHi is a hierarchical classification system designed for CITE-Seq data, but applicable to diverse single-cell sequencing modalities."""

    homepage = "https://github.com/donnafarberlab/MMoCHi/"
    git = "https://github.com/donnafarberlab/MMoCHi/"

    version("0.3.5", commit="b0f33874a45989d3d7305e80e6809f14509df1ef")


    depends_on("py-numpy@1.12.0:", type=("build", "run"))
    depends_on("py-pandas@1.0.5:", type=("build", "run"))
    depends_on("py-scikit-learn@1.1.2:", type=("build", "run"))
    depends_on("py-imbalanced-learn@0.11.0:", type=("build", "run"))
    depends_on("py-scipy@1.8.0:", type=("build", "run"))
    depends_on("py-scanpy@1.7.2:", type=("build", "run"))
    depends_on("py-anndata@0.8.0:", type=("build", "run"))
    depends_on("py-treelib@1.6.1:", type=("build", "run"))
    depends_on("py-matplotlib@3.6.1:", type=("build", "run"))
    depends_on("py-ipywidgets@7.7.0:", type=("build", "run"))
    depends_on("py-pydot@1.4.2:", type=("build", "run"))
    depends_on("py-tqdm@4.64.0:", type=("build", "run"))
    depends_on("py-scikit-fda@0.5:", type=("build", "run"))
    depends_on("py-seaborn@0.12.2:", type=("build", "run"))
    depends_on("py-ipython@8.4.0:", type=("build", "run"))
    depends_on("py-ipykernel@6.18.0:", type=("build", "run"))
    depends_on("py-tqdm@4.64.0:", type=("build", "run"))
    depends_on("py-leidenalg@0.8.9:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        self.spec["python"].command("-c", "import mmochi")
