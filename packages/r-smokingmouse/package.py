# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmokingmouse(RPackage):
    """Provides access to smokingMouse project data

    This is an ExperimentHub package that provides access to the data at the gene, exon, transcript and junction level used in the analyses of the smokingMouse project. See https://github.com/LieberInstitute/smokingMouse_Indirects. This datasets contain the expression counts of genes, transcripts, exons and exon-exon junctions across 208 mice samples from pup and adult brains and adult blood. They also contain relevant information of these samples and features, such as conditions, QC metrics and if they were used after filtering steps and also if the features were differently expressed in the different experiments.
    """

    homepage = "https://github.com/LieberInstitute/smokingMouse"
    bioc = "smokingMouse"

    version("1.6.0", commit="ca897b9f5e08acbca31e02d0113e3a85b7ef9023")
    version("1.0.0", commit="cb8ad94632c5bd4520ff0992612208408959b196")
