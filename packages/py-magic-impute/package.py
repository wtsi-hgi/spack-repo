# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

class PyMagicImpute(PythonPackage):
    """Markov Affinity-based Graph Imputation of Cells (MAGIC) is an algorithm for denoising high-dimensional data most commonly applied to single-cell RNA sequencing data. """

    homepage = "https://github.com/KrishnaswamyLab/MAGIC"
    
    pypi = "magic-impute/magic-impute-3.0.0.tar.gz"
    
    version('3.0.0', sha256='0c3f6d17baf586c412c174709a19164f04e693fd1933a8c0399ae5c5bf1cfd7a')
    version('2.0.4', sha256='c97f16ff3f52b171da482ba4dd44617dae35a88ecfd17ddc4239ab24471e7839')
    version('2.0.3', sha256='81c831301a59a0bc5a2ff874536e840ae4a30bf8ea938d9607fd228c7c58a423')
    version('2.0.2', sha256='824d62174c206d641a1c09ec364d0241f2edfe32292a6607ba3fafa0a2d771c9')
    version('2.0.0', sha256='a209a310de46477abbadf0a720b76c10e49e905e1a2dcc4b9fdc342129c19aea')
    version('1.5.7', sha256='7af95173fb4312443e62713762dbf9ff75d852b7f50c3dc1562db6d725f88e23')
    version('1.5.6', sha256='0e9e977afdba59525ee919ed062c3fbfe77c11790cb092bc40bdc75442325991')
    version('1.5.5', sha256='ff8b39ed5422890040972d6933f9b2d6f4578a81a2f3a754d2e83c8ad77a5dcb')
    version('1.5.3', sha256='237656c37942a4e4cb7f000f5861b4eac40b3273df15f2f943b31d39cf3afc92')
    version('1.5.2', sha256='57d7f241d6e3e8ce6704819f28b1ab10a9ebd02290aad3ce25c4ba0b41511a55')
    version('1.5.1', sha256='8874bbf2c798097b837cd42b651df6f606b0dadd0e11758e79140c42f6e80e6d')
    version('1.5.0', sha256='9149588f6d10876290393e49d11faffc3f7aa15e1d38fa266699279b38b412e1')
    version('1.4.0', sha256='958aadfb67f70e3dc571a62134142711ea267c6327632872d531d52010688401')

    depends_on("py-setuptools", type="build")
