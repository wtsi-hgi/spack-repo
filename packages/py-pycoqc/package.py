# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
import os

class PyPycoqc(PythonPackage):
    """PycoQC computes metrics and generates interactive QC plots for Oxford Nanopore technologies sequencing data"""

    homepage = "https://github.com/a-slide/pycoQC"
    git = "https://github.com/a-slide/pycoQC"
    pypi = "pycoQC/pycoQC-2.5.2.tar.gz"

    version("2.5.2", sha256="8ceba86bb9a08bdf7c329a165d0218ad8b026f6772efa661fcc98750acc2c8ce")

    depends_on("python@3.6:", type=("build", "run"))
    depends_on("py-setuptools", type="build")

    depends_on("py-numpy@1.19:", type=("build", "run"))
    depends_on("py-scipy@1.5:", type=("build", "run"))
    depends_on("py-pandas@1.1:", type=("build", "run"))
    depends_on("py-plotly@4.1.0", type=("build", "run"))
    depends_on("py-jinja2@2.10:", type=("build", "run"))
    depends_on("py-h5py@3.1:", type=("build", "run"))
    depends_on("py-tqdm@4.54:", type=("build", "run"))
    depends_on("py-pysam@0.16:", type=("build", "run"))

    depends_on("py-retrying", type=("build", "run"))
