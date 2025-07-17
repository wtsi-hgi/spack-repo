# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenproseq(RPackage):
    """Generating Protein Sequences with Deep Generative Models

    Generative modeling for protein engineering is key to solving fundamental problems in synthetic biology, medicine, and material science. Machine learning has enabled us to generate useful protein sequences on a variety of scales. Generative models are machine learning methods which seek to model the distribution underlying the data, allowing for the generation of novel samples with similar properties to those on which the model was trained. Generative models of proteins can learn biologically meaningful representations helpful for a variety of downstream tasks. Furthermore, they can learn to generate protein sequences that have not been observed before and to assign higher probability to protein sequences that satisfy desired criteria. In this package, common deep generative models for protein sequences, such as variational autoencoder (VAE), generative adversarial networks (GAN), and autoregressive models are available. In the VAE and GAN, the Word2vec is used for embedding. The transformer encoder is applied to protein sequences for the autoregressive model.
    """

    bioc = "GenProSeq"

    version("1.12.0", commit="6cd2cb2c490a09fe5f023e5dff67b94d21942c69")
    version("1.6.0", commit="b262d9140bb272cf425f4908ada8ee502c69b545")

    depends_on("r-keras", type=("build", "run"))
    depends_on("r-mclust", type=("build", "run"))
    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-tensorflow", type=("build", "run"))
    depends_on("r-word2vec", type=("build", "run"))
    depends_on("r-deeppincs", type=("build", "run"))
    depends_on("r-ttgsea", type=("build", "run"))
    depends_on("r-catencoders", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
