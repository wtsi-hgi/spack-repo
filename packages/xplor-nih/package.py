# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class XplorNih(Package):
    """A System for X-ray Crystallography and NMR."""

    homepage = "https://nmr.cit.nih.gov/xplor-nih/"
    url = "https://bit.niddk.nih.gov/xplor-nih/packages/xplor-nih-3.8-Linux_x86_64.tar.gz"

    version("3.8", sha256="e81e2b147a981bc1ea75de718da3b49f20019cb94232579faea8020f0b50cbb6")

    resource(name="db", url="https://bit.niddk.nih.gov/xplor-nih/packages/xplor-nih-3.8-db.tar.gz", sha256="c0966a7f9a287687861e6a545306b72315671d52ff70e1621c395884df04c842", when="@3.8")

    depends_on("bc", type=("build", "link", "run"))
    depends_on("python", type=("build", "link", "run"))

    def install(self, spec, prefix):
        cd("..")
        move(self.stage.source_path, prefix.opt.xplornih)
        cd(prefix.opt.xplornih)
        mkdir(prefix.bin)
        which("./configure")("-symlinks", prefix.bin)
