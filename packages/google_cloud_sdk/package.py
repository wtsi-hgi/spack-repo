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
#     spack install google-cloud-sdk
#
# You can edit this file again by typing:
#
#     spack edit google-cloud-sdk
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class GoogleCloudSdk(Package):
    """Google Cloud SDK."""

    homepage = "https://cloud.google.com/sdk/docs/downloads-versioned-archives"
    url = "https://storage.googleapis.com/cloud-sdk-release/google-cloud-cli-485.0.0-linux-x86_64.tar.gz"
    license("Apache 2.0")

    version("485.0.0", sha256="d5cb04c857f50f776794ee77fe0598460bf8aa0b889ef5fd8f9828b8b9b124a0")

    depends_on("python")

    def install(self, spec, prefix):
        install_tree(".", self.prefix)
        Executable(join_path(self.prefix, "install.sh"))("-q")
