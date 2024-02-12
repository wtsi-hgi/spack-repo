# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyRichArgparse(PythonPackage):
    """rich-argparse improves the look and readability of argparse's help while requiring minimal changes to the code."""

    homepage = "https://github.com/hamdanal/rich-argparse"
    pypi = "rich_argparse/rich_argparse-1.4.0.tar.gz"

    version("1.4.0", sha256="c275f34ea3afe36aec6342c2a2298893104b5650528941fb53c21067276dba19")

    depends_on("py-hatchling", type="build")

    depends_on("py-rich", type=("build", "run"))
