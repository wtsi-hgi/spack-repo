# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from pathlib import Path
import llnl.util.tty as tty

class RstudioServer(Package):
    """RStudio Server."""

    homepage = "https://posit.co/products/open-source/rstudio"
    url_fmt = "https://download2.rstudio.org/server/bionic/amd64/rstudio-server-{0}-amd64.deb"
    url = url_fmt.format("1.2.3")

    version("2023.03.0-386", expand=False, sha256="8dcc6003cce4cf41fbbc0fd2c37c343311bbcbfa377d2e168245ab329df835b5")

    def url_for_version(self, version):
        return self.url_fmt.format(version)

    depends_on("sqlite", type="run")

    def install(self, spec, prefix):
        apt = which("apt-get")
        apt("install", self.stage.archive_file)
        path = Path("lib/rstudio-server")
        dest = Path(prefix) / path
        dest.mkdir(parents=True)
        src = Path("/usr") / path
        install_tree(str(src), str(dest))
