# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyEdlib(PythonPackage):
    """Lightweight, super fast library for sequence
    alignment using edit (Levenshtein) distance."""

    homepage = "https://pypi.org/project/edlib/"
    pypi = "edlib/edlib-1.3.9.tar.gz"

    version("1.3.9", sha256="b0fb6e85882cab02208ccd6daa46f80cb9ff1d05764e91bf22920a01d7a6fbfa", url="https://files.pythonhosted.org/packages/0c/dd/caa71ef15b46375e01581812e52ec8e3f4da0686f370e8b9179eb5f748fb/edlib-1.3.9.post1.tar.gz")

    depends_on("py-setuptools", type="build")
