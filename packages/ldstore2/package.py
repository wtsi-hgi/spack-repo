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
#     spack install ldstore2
#
# You can edit this file again by typing:
#
#     spack edit ldstore2
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Ldstore2(Package):
    """LDstore2 is a computationally efficient program for estimating and storing
    Linkage Disequilibrium (SNP correlations). It implements parallel processing
    using OpenMP and stores SNP correlations with SNP information in binary files
    for fast lookups."""

    homepage = "http://www.christianbenner.com"
    url = "http://www.christianbenner.com/ldstore_v2.0_x86_64.tgz"

    maintainers("zrb", "github_user2")

    version("2.0", sha256="be80818e2cdb5d223a15805b1fcf7569ba2b045a29bc02ca3e08af2eba95325f")

    depends_on("zstd")  # Required for compression support

    def install(self, spec, prefix):
        # Binary distribution - just copy executable to bin directory
        mkdirp(prefix.bin)
        install("ldstore_v2.0_x86_64", join_path(prefix.bin, "ldstore2"))
