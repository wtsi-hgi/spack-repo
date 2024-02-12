# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyCtxcore(PythonPackage):
    """Core functions for pycisTarget and the SCENIC tool suite"""

    homepage = "https://github.com/aertslab/ctxcore"
    url = "https://files.pythonhosted.org/packages/57/be/b60e62d10d80c80c5492739d6f2833ca2973bbc4088fcecf7053b5719da7/ctxcore-0.2.0-py3-none-any.whl"

    version("0.2.0", sha256="b90570377e26280c4861ebad1f4cee2fe598167c5d4bd12c1b713f03c9682627", expand=False)

    depends_on("py-cytoolz", type=("build", "run"))
    depends_on("py-frozendict", type=("build", "run"))
    depends_on("py-numba@0.51.2:", type=("build", "run"))
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pandas@0.24:", type=("build", "run"))
    depends_on("py-pyarrow@8.0.0:", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
