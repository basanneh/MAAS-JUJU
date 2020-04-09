#!/bin/bash

# export env for charms

baseDir=mycharms
newdir=charms01
export CHARM_DIR=$HOME/${baseDir}/${newdir}
export CHARM_LAYERS_DIR=$CHARM_DIR/layers
export CHARM_INTERFACES_DIR=$CHARM_DIR/interfaces

mkdir -p $CHARM_LAYERS_DIR $CHARM_INTERFACES_DIR

cd $CHARM_DIR/layers
