# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyNbsphinxLink(PythonPackage):
    """A sphinx extension for including notebook files from outside the sphinx source root."""

    homepage = "https://github.com/vidartf/nbsphinx-link"
    pypi = "nbsphinx-link/nbsphinx-link-1.3.0.tar.gz"

    version("1.3.0", sha256="fa3079a74c0dff1b2079e79a34babe770706ba8aa9cc0609c6dbfd593461a077")

    depends_on("py-nbsphinx", type=("build", "run"))
    depends_on("py-sphinx@1.8:", type=("build", "run"))
