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
#     spack install jasmine
#
# You can edit this file again by typing:
#
#     spack edit jasmine
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Jasmine(Package):
    """
    Jasmine predicts 5-Methylcytosine (5mC) of each CpG site in PacBio HiFi reads,
    using a Convolutional Neural Network. The jasmine model supports the Sequel II
    and Revio systems. Methylation is assumed to be symmetric between strands.
    The output is reported in the forward direction with respect to the HiFi
    read sequence.
    """

    homepage = "https://github.com/pacificbiosciences/jasmine"
    url = "https://github.com/PacificBiosciences/jasmine/releases/download/v2.0.0/jasmine"

    license("BSD 3-Clause Clear License")

    version("2.0.0", sha256="7a93e2b3932ed4701ae437f69a9c82b00b6b0718998ba2b137e0b06df0272e1c", expand=False)

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/jasmine", prefix.bin.jasmine)
        chmod = which("chmod")
        chmod("+x", prefix.bin.jasmine)
