# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyDropbox(PythonPackage):
    """The offical Dropbox SDK for Python."""

    homepage = "http://www.dropbox.com/developers"
    pypi = "dropbox/dropbox-11.36.2.tar.gz"

    version("11.36.2", sha256="d48d3d16d486c78b11c14a1c4a28a2611fbf5a0d0a358b861bfd9482e603c500")

    depends_on("py-setuptools", type="build")

    depends_on("py-requests@2.16.2:", type=("build", "run"))
    depends_on("py-six@1.12.0:", type=("build", "run"))
    depends_on("py-stone@2:", type=("build", "run"))
