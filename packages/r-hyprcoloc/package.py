# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyprcoloc(RPackage):
    """Hypothesis Prioritisation in multi-trait Colocalization (HyPrColoc)."""

    homepage = "https://github.com/jrs95/hyprcoloc"
    url = "https://github.com/jrs95/hyprcoloc/archive/refs/tags/v0.0.2.tar.gz"
    git = "https://github.com/jrs95/hyprcoloc.git"

    version("0.0.2", sha256="333303cefce724fdd66f92ba822c75cbb0f463e36f3391e6d162efa69ef2e921")
    version("0.0.1", sha256="00f5a1a5c160e53185b08eb4761a29ed8602804dc9334b291709ded27df19e40")

    def patch(self):
        """Ensure Eigen receives integral indices when slicing."""

        align2_replacements = {
            "tmp_rho(i) = RHO(snps1(1 , i)-1, snps1(0 , i)-1);": "tmp_rho(i) = RHO(static_cast<Eigen::Index>(snps1(1, i)) - 1, static_cast<Eigen::Index>(snps1(0, i)) - 1);",
            "snp_cor_1cv(2*m) = RHO(snps1(0,i)-1, j2)*tet_1cv(2*m);": "snp_cor_1cv(2*m) = RHO(static_cast<Eigen::Index>(snps1(0, i)) - 1, j2)*tet_1cv(2*m);",
            "snp_cor_1cv(2*m+1) = RHO(snps1(1,i)-1, j2)*tet_1cv(2*m+1);": "snp_cor_1cv(2*m+1) = RHO(static_cast<Eigen::Index>(snps1(1, i)) - 1, j2)*tet_1cv(2*m+1);",
            "snp_cor_2cv(2*m) = RHO(snps1(0,i)-1, snps1(0,j2)-1)*tet_2cv(2*m);": "snp_cor_2cv(2*m) = RHO(static_cast<Eigen::Index>(snps1(0, i)) - 1, static_cast<Eigen::Index>(snps1(0, j2)) - 1)*tet_2cv(2*m);",
            "snp_cor_2cv(2*m+1) = RHO(snps1(1,i)-1, snps1(0,j2)-1)*tet_2cv(2*m+1);": "snp_cor_2cv(2*m+1) = RHO(static_cast<Eigen::Index>(snps1(1, i)) - 1, static_cast<Eigen::Index>(snps1(0, j2)) - 1)*tet_2cv(2*m+1);",
            "snp_cor_2cv_1(2*m) = RHO(snps1(0,i)-1, snps1(1,j2)-1)*tet_2cv(2*m);": "snp_cor_2cv_1(2*m) = RHO(static_cast<Eigen::Index>(snps1(0, i)) - 1, static_cast<Eigen::Index>(snps1(1, j2)) - 1)*tet_2cv(2*m);",
            "snp_cor_2cv_1(2*m+1) = RHO(snps1(1,i)-1, snps1(1,j2)-1)*tet_2cv(2*m+1);": "snp_cor_2cv_1(2*m+1) = RHO(static_cast<Eigen::Index>(snps1(1, i)) - 1, static_cast<Eigen::Index>(snps1(1, j2)) - 1)*tet_2cv(2*m+1);",
            "sigZ2(2*ncolZco+1, 2*ncolZco) = RHO(snps1(1 , j2)-1, snps1(0 , j2)-1);": "sigZ2(2*ncolZco+1, 2*ncolZco) = RHO(static_cast<Eigen::Index>(snps1(1, j2)) - 1, static_cast<Eigen::Index>(snps1(0, j2)) - 1);",
            "sigZ2(2*ncolZco, 2*ncolZco+1) = RHO(snps1(1 , j2)-1, snps1(0 , j2)-1);": "sigZ2(2*ncolZco, 2*ncolZco+1) = RHO(static_cast<Eigen::Index>(snps1(1, j2)) - 1, static_cast<Eigen::Index>(snps1(0, j2)) - 1);",
        }

        for old, new in align2_replacements.items():
            filter_file(old, new, "src/align2.cpp", string=True)

        filter_file(
            "tmp_rho(i) = RHO(snps(0 , i)-1, snps(1 , i)-1);",
            "tmp_rho(i) = RHO(static_cast<Eigen::Index>(snps(0, i)) - 1, static_cast<Eigen::Index>(snps(1, i)) - 1);",
            "src/regional2.cpp",
            string=True,
        )

    depends_on("r@3.6.0:", type=("build", "run"))
    depends_on("r-iterpc", type=("build", "run"))
    depends_on("r-rcpp", type=("build", "run", "link"))
    depends_on("r-rcppeigen", type=("build", "run", "link"))
    depends_on("r-rmpfr", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-pheatmap", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
