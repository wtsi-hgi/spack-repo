# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class PyPdbfixer(PythonPackage):
    """PDBFixer is an easy to use application for fixing problems in
    Protein Data Bank files in preparation for simulating them."""

    homepage = "https://github.com/openmm/pdbfixer"
    url = "https://github.com/openmm/pdbfixer/archive/refs/tags/1.9.tar.gz"

    version("1.9", sha256="88b9a77e50655f89d0eb2075093773e82c27a4cef842cb7d735c877b20cd39fb")
    version("1.8.1", sha256="d50551abfe9dbaefc066f4d9d400cdebe57f1fefd9de9d01e12beb87efd99595")
    version("1.7", sha256="a0bef3c52a7bbe69a6aea5333f51f3e7d158339be5829aed19b0344bd66d4eea")

    depends_on("py-setuptools", type="build")
    depends_on("openmm@7.1:7.5", type=("build", "run"), when="@1.7")
    depends_on("openmm@7.6:", type=("build", "run"), when="@1.8:")
    depends_on("openmm@8.0.0:", type=("build", "run"), when="@1.9")
    depends_on("py-numpy", type=("build", "run"))
