# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPyensembl(PythonPackage):
    """Python interface to Ensembl reference genome metadata."""

    homepage = "https://github.com/openvax/pyensembl"
    pypi = "pyensembl/pyensembl-2.2.3.tar.gz"

    version("2.2.3", sha256="96d96c1a6823657f0f581b0c22a314e1a34b80a832dd756f0e5217d51356e96a")

    depends_on("py-setuptools", type="build")
    depends_on("py-typechecks@0.0.2:", type=("build", "run"))
    depends_on("py-datacache@1.1.4:", type=("build", "run"))
    depends_on("py-memoized-property@1.0.2:", type=("build", "run"))
    depends_on("py-tinytimer", type=("build", "run"))
    depends_on("py-gtfparse@1.3.0:", type=("build", "run"))
    depends_on("py-serializable", type=("build", "run"))
    depends_on("py-nose@1.3.3:", type=("build", "run"))
    depends_on("py-pylint@1.4.4:", type=("build", "run"))

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            python("-c", "import pyensembl")
