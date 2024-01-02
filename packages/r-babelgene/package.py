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
#     spack install r-babelgene
#
# You can edit this file again by typing:
#
#     spack edit r-babelgene
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RBabelgene(RPackage):
    """Gene Orthologs for Model Organisms in a Tidy Data Format

    Genomic analysis of model organisms frequently requires the use of databases based on human data or making comparisons to patient-derived resources. This requires harmonization of gene names into the same gene space. The 'babelgene' R package converts between human and non-human gene orthologs/homologs. The package integrates orthology assertion predictions sourced from multiple databases as compiled by the HGNC Comparison of Orthology Predictions (HCOP) (Wright et al. 2005 <doi:10.1007/s00335-005-0103-2>, Eyre et al. 2007 <doi:10.1093/bib/bbl030>, Seal et al. 2011 <doi:10.1093/nar/gkq892>).
    """


    homepage = "https://igordot.github.io/babelgene/"
    cran = "babelgene"

    version("22.9", sha256="ce6601dcb78352516d3b0355042c52a20e154b39d3b27b93ff52150a59c885e2")

    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
