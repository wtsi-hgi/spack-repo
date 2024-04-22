# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class Tmscore(Package):
    """TM-score is a metric for assessing the topological similarity of protein structures. It is designed to solve two major problems in traditional metrics such as root-mean-square deviation (RMSD): (1) TM-score weights smaller distance errors stronger than larger distance errors and makes the score value more sensitive to the global fold similarity than to the local structural variations; (2) TM-score introduces a length-dependent scale to normalize the distance errors and makes the magnitude of TM-score length-independent for random structure pairs. TM-score has the value in (0,1], where 1 indicates a perfect match between two structures. Following strict statistics of structures in the PDB, scores below 0.17 correspond to randomly chosen unrelated proteins whereas structures with a score higher than 0.5 assume generally the same fold in SCOP/CATH. The equation of TM-score can be found at Wikipedia or the original publication. Please read "Problem and Solution", if you have problem on how to calculate TM-score for protein/RNA/DNA structures."""

    homepage = "https://seq2fun.dcmb.med.umich.edu//TM-score/"
    
    version("2022-02-27", sha256="0058ba45be81c56a187f72ca30c11c8127ed96dffd158a9b6caa964c680c8f86", url="https://seq2fun.dcmb.med.umich.edu//TM-score/TMscore.cpp", expand=False)

    def install(self, spec, prefix):
        bin = join_path(self.prefix, "bin")
        mkdirp(bin)

        which("g++")("-static", "-O3", "-ffast-math", "-lm", "-o", join_path(bin, "TMscore"), self.stage.archive_file)

