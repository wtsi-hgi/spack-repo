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
#     spack install perl-npg-tracking
#
# You can edit this file again by typing:
#
#     spack edit perl-npg-tracking
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PerlNpgTracking(PerlPackage):
    """Illumina Sequencing Instruments Tracking."""

    homepage = "https://github.com/wtsi-npg/npg_tracking"
    url = "https://github.com/wtsi-npg/npg_tracking/archive/refs/tags/101.2.0.tar.gz"

    license("UNKNOWN")

    version("101.2.0", sha256="3455dda2e21fad61e13fbef3c6a80ad1c5420b620f054284ee2154ee0cc85d84")
    version("91.12.0", sha256="37670330d8349885aa954a2f2c838a3d7e3d9d9a54b3817286a3dafdcb78e65f")
    version("91.11.0", sha256="966a7bd988663b40fb39aba9d0a66e7bb4c41dabf5c4e8ce3b638256625f7576")
    version("91.10.0", sha256="1896eba4bd65607c3170e4cc7cc90a5d994f0e69202bbf89c8f65273ee905223")
    version("91.9.0", sha256="19295f7c2d1789a25f3265d466275568ce0613490d781ce7104dced8fde05d0c")
    version("91.8.0", sha256="07e31372766014c896e9aaa5dea674b772354192757e75d503cfff0738ed44f4")
    version("91.7.0", sha256="f7f5bfa5ffa7706af878ee698f4de393c56ab2b2cc72f27993e16aa821ef7822")
    version("91.6.0", sha256="4eb3087d05cd2c84f233af5704f4954b1027e6e723094fd8f9e43894db35d70d")
    version("91.4.0", sha256="b08d330576d03e275e3562270299bab3a1a99802577e90ee65bc32157cb22f96")
    version("91.3.0", sha256="f0c6d34ad9c3f9287bb28b3d08bbbc1d7c588830bc85589c2f5a8514725e2d2b")
    version("91.2.0", sha256="f783aeb40a3f074a33946403a383e33c69f99281b167412bb6565e9722fec43a")

    depends_on("perl-module-build", type="build")
    depends_on("perl-dnap-utilities", type=("build", "run"))
    depends_on("perl-readonly", type=("build", "run"))
    depends_on("perl-config-auto", type=("build", "run"))
    depends_on("perl-moosex-attributehelpers", type=("build", "run"))
    depends_on("perl-moosex-aliases", type=("build", "run"))
    depends_on("perl-moosex-role-parameterized", type=("build", "run"))
    depends_on("perl-moosex-storage", type=("build", "run"))
    depends_on("perl-string-rewriteprefix", type=("build", "run"))
    depends_on("perl-json-xs", type=("build", "run"))
