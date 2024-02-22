# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class PyGdown(PythonPackage):
    """Google Drive Public File Downloader when Curl/Wget Fails."""

    homepage = "https://github.com/wkentaro/gdown"
    pypi = "gdown/gdown-5.1.0.tar.gz"

    version("5.1.0", sha256="550a72dc5ca2819fe4bcc15d80d05d7c98c0b90e57256254b77d0256b9df4683")

    depends_on("py-hatchling", type=("build"))
    depends_on("py-hatch-fancy-pypi-readme", type=("build"))
    depends_on("py-hatch-vcs", type=("build"))

    depends_on("py-filelock", type=("build", "run"))
    depends_on("py-requests+socks", type=("build", "run"))
    depends_on("py-tqdm", type=("build", "run"))
    depends_on("py-beautifulsoup4", type=("build", "run"))
