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
#     spack install arriba
#
# You can edit this file again by typing:
#
#     spack edit arriba
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Arriba(MakefilePackage):
    """Arriba is a command-line tool for the detection of gene fusions from RNA-Seq data.

    It was developed for the use in a clinical research setting, with a focus on
    short runtimes and high sensitivity. It is based on the ultrafast STAR aligner,
    and the post-alignment runtime is typically just ~2 minutes. Arriba can detect
    gene fusions, viral integration sites, internal tandem duplications, whole exon
    duplications, and other structural rearrangements with potential clinical relevance."""

    homepage = "https://github.com/suhrig/arriba"
    url = "https://github.com/suhrig/arriba/archive/refs/tags/v2.5.0.tar.gz"

    license("MIT/Expat")

    version("2.5.0", sha256="562332dafffe620f7864a5ebc600049f16711f8e792acb77c14e003cdce69461")

    depends_on("star", type=("build", "run"))
    depends_on("r", type=("build", "run"))
    depends_on("r-circlize", type=("build", "run"))
    depends_on("r-genomicalignments", type=("build", "run"))
    depends_on("samtools", type=("build", "run"))

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        install("arriba", prefix.bin)
        install("draw_fusions.R", prefix.bin)
        install("run_arriba.sh", prefix.bin)
        install_tree("scripts", prefix.scripts)
