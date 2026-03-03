# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyRosetta(PythonPackage):
    """PyRosetta is a Python-based molecular modeling tool for simulating macromolecular structures.
    It is distributed under the PyRosetta Software Non-Commercial License Agreement."""

    homepage = "https://www.pyrosetta.org/"
    url = "https://west.rosettacommons.org/pyrosetta/release/release/PyRosetta4.Release.python310.linux.wheel/pyrosetta-2024.39+release.59628fb-cp310-cp310-linux_x86_64.whl"

    version(
        "2024.39",
        url="https://west.rosettacommons.org/pyrosetta/release/release/PyRosetta4.Release.python310.linux.wheel/pyrosetta-2024.39+release.59628fb-cp310-cp310-linux_x86_64.whl",
        sha256="4c02ef28820c7a9925842b86bf45a989163f941ddf30185c182896802fc96ec2",
        expand=False,
    )

    depends_on("py-setuptools", type="build")
    depends_on("python@3.10", type=("build", "run"))
