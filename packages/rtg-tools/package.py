# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install rtg-tools
#
# You can edit this file again by typing:
#
#     spack edit rtg-tools
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *
from pathlib import Path


class RtgTools(Package):
    """RTG Tools is a subset of RTG Core that includes several useful utilities for dealing with VCF files and sequence data. Probably the most interesting is the vcfeval command which performs sophisticated comparison of VCF files.."""

    homepage = "https://github.com/RealTimeGenomics/rtg-tools"
    url = "https://github.com/RealTimeGenomics/rtg-tools/archive/refs/tags/3.12.1.tar.gz"

    license("BSD-2-Clause")

    version("3.12.1", sha256="6ee0ffe1bba7b5497aa09b147a7525b77b1808e6a71368aad440cbd64658085c")
    version("3.12", sha256="1509e4cf22d8d97edf85ff6cb0d86a6eaf3bcc945bb933f2215708d43dc617d3")
    version("3.11", sha256="7410b476eb14f42959bb2f4c3c56d7e5b46da0f6bbafbac688d84cb05df7a2d4")
    version("3.10.1", sha256="395757713dd59f8db974385c3f82346b573b984dcfc22038c59194916cb2cb79")
    version("3.10", sha256="572a1926ac8c841bbd845f3975ed5fb3c72fe736346c82522bad3e35e840dd6b")
    version("3.9.1", sha256="e4738c236a5a1ad13754500b2078c9500d66051ac305abf96730015230c4f830")
    version("3.9", sha256="87f48bee0312ee02da51543ab499734dbef2b430a6999e131e0255f0eb9546af")
    version("3.8.4", sha256="203a5765c42a53ecdbf4a1ad2c1cd8b408d7754776388ef58365c80fc060dc3b")
    version("3.8.3", sha256="994ee7763996eb7bb861be3f53a5da94e8e37956f051ef9666ffe9ab48cbb6b2")
    version("3.8.2", sha256="9dfb5e127bd979785ddbd6b46671d94612f9a7bc00a5807d111df76b35a18d5f")

    depends_on("ant", type="build")
    depends_on("java@1.8:11", type=("build", "link", "run"))
    depends_on("graphviz+pangocairo", type=("build", "link", "run"))
    depends_on("libxrender", type=("build", "link", "run"))
    depends_on("libxtst", type=("build", "link", "run"))
    depends_on("libxi", type=("build", "link", "run"))

    def install(self, spec, prefix):
        ant = which("ant")
        ant("zip-nojre")
        zipfile = list(Path("dist").glob("*.zip"))[0]
        which("unzip")(str(zipfile), "-d", "dist")
        remove(zipfile)
        unzipped = list(Path("dist").glob("rtg-tools*"))[0]

        mkdir(prefix.bin)
        with working_dir(unzipped):
            filter_file(
                'read -r -p "Would you like to enable automatic usage logging (y/n)? " REPLY',
                "REPLY=y",
                "rtg",
                string=True,
            )

            install_tree("scripts", prefix.scripts)
            install("rtg", prefix.bin.rtg)
            install("RTG.jar", join_path(prefix.bin, "RTG.jar"))
            install_tree("third-party", join_path(prefix.bin, "third-party"))
            Executable(prefix.bin.rtg)("version")

    def setup_run_environment(self, env):
        for dep in self.spec.dependencies(deptype="run"):
            query = self.spec[dep.name]
            env.prepend_path("LD_LIBRARY_PATH", query.prefix.lib)
