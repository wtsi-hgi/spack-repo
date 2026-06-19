# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyOpenspliceai(PythonPackage):
    """OpenSpliceAI is an open‐source, efficient, and modular framework for splice site prediction. It is a reimplementation and extension of SpliceAI (Jaganathan et al., 2019) built on the modern PyTorch framework. OpenSpliceAI provides researchers with a user‐friendly suite of tools for studying transcript splicing - from creating training datasets and training models to predicting splice sites and assessing the impact of genetic variants."""

    homepage = "https://ccb.jhu.edu/openspliceai"
    pypi = "openspliceai/openspliceai-0.0.6.tar.gz"

    version("0.0.6", sha256="872a840bb513143f4499fdee79eccaefe9a49237a9767759e38abe727ab38d9c")

    depends_on("python@3.9:", type=("build", "run"))
    depends_on("py-setuptools", type="build")
    depends_on("py-pip@:22", type="build", when="^py-setuptools@:63")
    depends_on("py-pip@23:", type="build", when="^py-setuptools@64:")

    depends_on("py-h5py@3.9.0:", type=("build", "run"))
    depends_on("py-numpy@1.24.4:", type=("build", "run"))
    depends_on("py-gffutils@0.12:", type=("build", "run"))
    depends_on("py-pysam@0.22.0:", type=("build", "run"))
    depends_on("py-pandas@1.5.3:", type=("build", "run"))
    depends_on("py-pyfaidx@0.8.1.1:", type=("build", "run"))
    depends_on("py-tqdm@4.65.2:", type=("build", "run"))
    depends_on("py-torch@2.2.1:", type=("build", "run"))
    depends_on("py-torchaudio@2.2.1:", type=("build", "run"))
    depends_on("py-torchvision@0.17.1:", type=("build", "run"))
    depends_on("py-scikit-learn@1.4.1:", type=("build", "run"))
    depends_on("py-biopython@1.83:", type=("build", "run"))
    depends_on("py-matplotlib@3.8.3:", type=("build", "run"))
    depends_on("py-matplotlib-inline@0.1.7:", type=("build", "run"))
    depends_on("py-psutil@5.9.2:", type=("build", "run"))
    depends_on("py-mappy@2.28:", type=("build", "run"))
