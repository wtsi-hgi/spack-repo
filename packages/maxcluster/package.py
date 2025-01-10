# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Maxcluster(Package):
    """
    MaxCluster is a tool for protein structure comparison and clustering.
    """

    homepage = "https://www.sbg.bio.ic.ac.uk/~maxcluster/"
    url = "https://www.sbg.bio.ic.ac.uk/~maxcluster/maxcluster64bit"

    # Since no version is specified in the URL, we'll use a date-based version
    version("1.0", sha256="ca6dee8faf0649479d18c4d758cfdd01c71750e3093726b51646948605090aa6", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install("maxcluster64bit", prefix.bin.maxcluster)
        chmod = which("chmod")
        chmod("+x", prefix.bin.maxcluster)
