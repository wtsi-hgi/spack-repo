# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyScatacFragmentTools(PythonPackage):
    """Tools for working with scATAC-seq fragment files."""

    homepage = "https://github.com/aertslab/scatac_fragment_tools/"
    pypi = "scatac_fragment_tools/scatac_fragment_tools-0.1.0.tar.gz"

    version("0.1.0", sha256="e77a03ad1b7170c212f1ac672dad2c5d7e7f091b94e47b36a2ec2adc42051857")

    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pybigwig", type=("build", "run"))
    depends_on("py-pybigtools", type=("build", "run"))
    depends_on("py-polars", type=("build", "run"))
    depends_on("py-pyarrow", type=("build", "run"))
    depends_on("py-numba", type=("build", "run"))
    depends_on("py-rich-argparse", type=("build", "run"))
    depends_on("py-joblib", type=("build", "run"))
