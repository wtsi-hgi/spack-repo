# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBabelgene(RPackage):
    """Gene Orthologs for Model Organisms in a Tidy Data Format
    
    Genomic analysis of model organisms frequently requires the
    use of databases based on human data or making comparisons to
    patient-derived resources. This requires harmonization of gene names
    into the same gene space. The 'babelgene' R package converts between
    human and non-human gene orthologs/homologs. The package integrates
    orthology assertion predictions sourced from multiple databases as
    compiled by the HGNC Comparison of Orthology Predictions (HCOP)
    (Wright et al. 2005 <doi:10.1007/s00335-005-0103-2>, Eyre et al. 2007
    <doi:10.1093/bib/bbl030>, Seal et al. 2011 <doi:10.1093/nar/gkq892>).
    """

    homepage = "https://cran.r-project.org/web/packages/babelgene"
    
    cran = "babelgene"

    # versions
    version("22.9", md5="2fd77f846bb9dc07e2d1589f1d95fea5")
    

    # dependencies
    depends_on("r@3.4:", type=('build', 'run'))
    depends_on("r-dplyr", type=('build', 'run'))
    depends_on("r-rlang", type=('build', 'run'))
    
