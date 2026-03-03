# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgan(RPackage):
	"""Generative Adversarial Nets (GAN) in R

	An easy way to get started with Generative Adversarial Nets (GAN) in R. The GAN algorithm was initially 
    described by Goodfellow et al. 2014 <https://proceedings.neurips.cc/paper/2014/file/5ca3e9b122f61f8f06494c97b1afccf3-Paper.pdf>. A GAN can be used to learn the joint distribution of complex data by 
    comparison. A GAN consists of two neural networks a Generator and a Discriminator, where the two
    neural networks play an adversarial minimax game.
    Built-in GAN models make the training of GANs in R possible in one line and make it easy to 
    experiment with different design choices (e.g. different network architectures, value functions, optimizers).
    The built-in GAN models work with tabular data (e.g. to produce synthetic data) and image data. 
    Methods to post-process the output of GAN models to enhance the quality of samples are available.
	"""
	
	homepage = "https://github.com/mneunhoe/RGAN"
	cran = "RGAN" 

	version("0.1.1", md5="17ebfc4d9a9bf41a47611e85867d365d")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
