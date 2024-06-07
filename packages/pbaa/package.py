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
#     spack install pbaa
#
# You can edit this file again by typing:
#
#     spack edit pbaa
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Pbaa(Package):
    """
    PacBio Amplicon Analysis (pbaa) separates complex mixtures of amplicon targets from genomic samples.
    The pbaa application is designed to cluster and generate high-quality consensus sequences from HiFi reads.
    This application only works on HiFi amplicon data. There are several assumptions made within the code that
    will only support high quality reads (>QV20). This application will not work on CLR data. pbaa is reference
    aided method (pseudo de-novo).

    Typical use cases involve multi-allelic samples where the sample-specific ploidy or copy number is unknown.
    pbaa can effectively separate alleles with one to many variants, including SNVs and large indels contained
    within the target region. pbaa has been optimized and tested for datasets with a moderate to high (<50)
    cluster counts.
    """

    homepage = "https://github.com/PacificBiosciences/pbAA"
    url = "https://github.com/PacificBiosciences/pbAA/releases/download/1.0.3/pbaa"

    license("BSD-3-Clause-Clear license")

    version("1.0.3", sha256="39ee21fc8b94d15f2004afeb34c6370bcb7661f8e29d35ebd50349f0dced472c", expand=False)

    def install(self, spec, prefix):
        mkdir(prefix.bin)
        install(self.stage.source_path + "/pbaa", prefix.bin.pbaa)
        chmod = which("chmod")
        chmod("+x", prefix.bin.pbaa)
