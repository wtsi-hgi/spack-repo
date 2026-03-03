# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHurryFilesize(PythonPackage):
    """A simple Python library for human readable file sizes (or anything sized in bytes)."""

    homepage = "UNKNOWN"
    pypi = "hurry.filesize/hurry.filesize-0.9.tar.gz"

    version("0.9", sha256="f5368329adbef86accd3bc9490522340bb79260455ae89b1a42c10f63801b9a6")

    depends_on("py-setuptools", type="build")
