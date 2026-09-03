class_name Enemy
extends Node2D

@export_category("Life")
@export var health: int = 10
@export var death_prefab: PackedScene
@onready var damage_digit_marker = $DamageDigitMarker

var damage_digit_prefab: PackedScene

@export_category("Drop")
@export var drop_chance:float
@export var drop_itens:Array[PackedScene]
@export var drop_chances:Array[float]

func _ready():
	damage_digit_prefab = preload("res://life/damage_digit.tscn")

func damage(amount: int) -> void:
	health -= amount
	print("Inimigo recebeu dano de ", amount, ". A vida total é de ", health)
	modulate = Color.RED
	var tween = create_tween()
	tween.set_ease(Tween.EASE_IN)
	tween.set_trans(Tween.TRANS_QUINT)
	tween.tween_property(self, "modulate", Color.WHITE, 0.3)
	var damage_digit = damage_digit_prefab.instantiate()
	damage_digit.value = amount
	if damage_digit_marker:
		damage_digit.global_position = damage_digit_marker.global_position
	else:
		damage_digit.global_position = global_position
	get_parent().add_child(damage_digit)
	if health <= 0:
		die()

func die() -> void:
	if death_prefab:
		var death_object = death_prefab.instantiate()
		death_object.position = position
		get_parent().add_child(death_object)
	if randf() <= drop_chance:
		drop_item()
	GameManager.monsters_defeated_counter += 1
	queue_free()

func get_random_drop_item() -> PackedScene:
	if drop_itens.size() == 1:
		return drop_itens[0]
	var max_chance:float = 0.0
	for drop_chance in drop_chances:
		max_chance += drop_chance
	var random_value = randf() * max_chance
	var agulha:float = 0.0
	for i in drop_itens.size():
		var drop_itens = drop_itens[i]
		var drop_chance = drop_chances[i] if i < drop_chances.size() else 1
		if random_value <= drop_chance + agulha:
			return drop_itens
		agulha += drop_chance
	return drop_itens[0]

func drop_item() -> void:
	var drop = get_random_drop_item().instantiate()
	drop.position = position
	get_parent().add_child(drop)
