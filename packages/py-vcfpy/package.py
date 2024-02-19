# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyVcfpy(PythonPackage):
    """Python 3 VCF library with good support for both reading and writing."""

    homepage = "https://github.com/bihealth/vcfpy"
    pypi = "vcfpy/vcfpy-0.13.8.tar.gz"

    version("0.13.8", sha256="e7d00965105e7ca9567299f073ad60c6bbfc78d685d25ba33353988af9b33160")

    depends_on("py-setuptools", type="build")

    depends_on("py-pysam@0.10.0:", type=("build", "run"))
