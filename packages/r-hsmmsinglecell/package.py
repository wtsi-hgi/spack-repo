# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsmmsinglecell(RPackage):
    """Single-cell RNA-Seq for differentiating human skeletal muscle myoblasts (HSMM)

    Skeletal myoblasts undergo a well-characterized sequence of morphological and transcriptional changes during differentiation. In this experiment, primary human skeletal muscle myoblasts (HSMM) were expanded under high mitogen conditions (GM) and then differentiated by switching to low-mitogen media (DM).  RNA-Seq libraries were sequenced from each of several hundred cells taken over a time-course of serum-induced differentiation. Between 49 and 77 cells were captured at each of four time points (0, 24, 48, 72 hours) following serum switch using the Fluidigm C1 microfluidic system. RNA from each cell was isolated and used to construct mRNA-Seq libraries, which were then sequenced to a depth of ~4 million reads per library, resulting in a complete gene expression profile for each cell.
    """

    bioc = "HSMMSingleCell"

    version("1.28.0", commit="cdf07e9b9f572ee781186bcac377c71682f4f74a")
    version("1.22.0", commit="2e54e3df8c6761fb53896b46c1f6dd3f42abb990")

    depends_on("r@2.10:", type=("build", "run"))
