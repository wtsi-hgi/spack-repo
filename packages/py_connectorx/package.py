# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyConnectorx(PythonPackage):
    """ConnectorX enables you to load data from databases into Python in the fastest and most memory efficient way."""

    url = "https://files.pythonhosted.org/packages/38/9c/3a3a831bfbd30fdedd61994d35df41fd0d47145693fe706976589214f811/connectorx-0.3.2-cp311-cp311-manylinux_2_28_x86_64.whl"

    version("0.3.2-py311", sha256="9403902685b3423cba786db01a36f36efef90ae3d429e45b74dadb4ae9e328dc", expand=False, url="https://files.pythonhosted.org/packages/38/9c/3a3a831bfbd30fdedd61994d35df41fd0d47145693fe706976589214f811/connectorx-0.3.2-cp311-cp311-manylinux_2_28_x86_64.whl")
    version("0.3.2-py310", sha256="3f6431a30304271f9137bd7854d2850231041f95164c6b749d9ede4c0d92d10c", expand=False, url="https://files.pythonhosted.org/packages/37/26/03d1a9d461dd770a360d9eaab2e01cd418b3fc6724ec2e5ec3d9cde65418/connectorx-0.3.2-cp310-cp310-manylinux_2_28_x86_64.whl")
    version("0.3.2-py309", sha256="74f5b93535663cf47f9fc3d7964f93e652c07003fa71c38d7a68f42167f54bba", expand=False, url="https://files.pythonhosted.org/packages/12/02/39741cb4e0495dc4ee1f4eb4fbd0cba704f2811770fe5aa682af7b663659/connectorx-0.3.2-cp39-cp39-manylinux_2_28_x86_64.whl")
    version("0.3.2-py308", sha256="c4387bb27ba3acde0ab6921fdafa3811e09fce0db3d1f1ede8547d9de3aab685", expand=False, url="https://files.pythonhosted.org/packages/ff/d0/c69a0285b36eea11d93a78eae0fc4580e708f7d19672608de4dae6edfb16/connectorx-0.3.2-cp38-cp38-manylinux_2_28_x86_64.whl")

    depends_on("python@3.11", when="@0.3.2-py311")
    depends_on("python@3.10", when="@0.3.2-py310")
    depends_on("python@3.9", when="@0.3.2-py309")
    depends_on("python@3.8", when="@0.3.2-py308")
