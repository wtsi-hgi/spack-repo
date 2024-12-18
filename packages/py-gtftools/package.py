# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGtftools(PythonPackage):
    """gtftools provides a set of functions to compute or extract various features of gene models."""

    homepage = "https://pypi.org/project/gtftools/"
    pypi = "gtftools/gtftools-0.9.0.tar.gz"

    version("0.9.0", sha256="7dfc0f8ecb8c5d34fee26aa3981c2393cee0419dcf3e51a70d7896c8c393f3fd")

    depends_on("py-setuptools", type=("build"))
