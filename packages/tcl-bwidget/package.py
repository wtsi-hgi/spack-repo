# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *
from pathlib import Path


class TclBwidget(Package):
    """The BWidget Toolkit is a high-level Widget Set for Tcl/Tk built using
    native Tcl/Tk 8.x namespaces.

    The BWidgets have a professional look&feel as in other well known
    Toolkits (Tix or Incr Widgets), but the concept is radically different
    because everything is pure Tcl/Tk.  No platform dependencies, and no
    compiling required.  The code is 100% Pure Tcl/Tk.

    The BWidget library was originally developed by UNIFIX Online, and
    released under both the GNU Public License and the Tcl license.
    BWidget is now maintained as a community project, hosted by
    Sourceforge.  Scores of fixes and enhancements have been added by
    community developers.  See the ChangeLog file for details.
    """

    homepage = "https://core.tcl-lang.org/bwidget/home"
    url = "https://sourceforge.net/projects/tcllib/files/BWidget/1.9.16/bwidget-1.9.16.tar.gz"
    list_url = "https://sourceforge.net/projects/tcllib/files/BWidget/"
    list_depth = 1

    license("TCL")

    version("1.9.16", sha256="bfe0036374b84293d23620a7f6dda86571813d0c7adfed983c1f337e5ce81ae0")
    version("1.9.14", sha256="8e9692140167161877601445e7a5b9da5bb738ce8d08ee99b016629bc784a672")
    version("1.9.13", sha256="76d8f42280e7160242186d12437949830eabd5009a6c14f4e7dba0f661403a81")
    version("1.9.12", sha256="2f682da93e07ff8cadd6c0580e7d4de3c8828134eab662dbe3d0e6ffc9443263")
    version("1.9.11", sha256="448a1db08a4ca477ce339dfe592fd85c4c0649c3ff554fb4e86d6826d39bc8b9")
    version("1.9.10", sha256="26c312204bd9d065001e95fcac8fed0f63cb44e746204853f21813ac62aeb408")
    version("1.9.9", sha256="b0e943b31b3513e9cc9a49e3f71d8b895ab55f5c8dfeaf849c8c308697f13573")
    version("1.9.8", sha256="545016e3ee998991308f54d8ef26bbf16144ee50fa432b9100d37ef806bdb314")
    version("1.9.7", sha256="e6668592c26d21558370335c42c1e85368d40706cc84b38fca01bc40e8395ffc")
    version("1.9.6", sha256="155e9cf2c6973956a0bbde450f2df358ce1eb97a2b2950d0681a36f861e67553")
    version("1.9.5", sha256="313229892075fecbe57eef63525a901f384822e67de67b06749a2ab7a5d45ada")
    version("1.9.4", sha256="f2761ee2ac1d95c36e095bf16f63f02e8b8418c9516853b746034bfb3029563e")
    version("1.9.3", sha256="87af601a699c64a613198c6726c519dac160c334ddeab4aaa967ffa8e6c1e9c7")

    extends("tcl")

    def install(self, spec, prefix):
        lib_dir = join_path(prefix.lib, "bwidget{}".format(self.version))
        mkdirp(lib_dir)
        for tcl in Path(self.stage.source_path).glob("*.tcl"):
            install(str(tcl), join_path(lib_dir, tcl.name))
