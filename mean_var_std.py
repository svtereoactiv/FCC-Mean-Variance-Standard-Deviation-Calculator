import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError("List must contain nine numbers.")

  calc = np.array(list).reshape((3,-1))

  formula = {
    'mean' : [
    np.mean(calc, axis=0).tolist(),
    np.mean(calc, axis=1).tolist(), 
    np.mean(calc).tolist()],
    'variance' : [
    np.var(calc, axis=0).tolist(), 
    np.var(calc, axis=1).tolist(), 
    np.var(calc).tolist()],
    'standard deviation' : [
    np.std(calc, axis=0).tolist(), 
    np.std(calc, axis=1).tolist(), 
    np.std(calc).tolist()],
    'max' : [
    np.max(calc, axis=0).tolist(), 
    np.max(calc, axis=1).tolist(), 
    np.max(calc).tolist()],
    'min' : [
    np.min(calc, axis=0).tolist(), 
    np.min(calc, axis=1).tolist(), 
    np.min(calc).tolist()],
    'sum' : [
    np.sum(calc, axis=0).tolist(), 
    np.sum(calc, axis=1).tolist(), 
    np.sum(calc).tolist()]
  }

  return formula



